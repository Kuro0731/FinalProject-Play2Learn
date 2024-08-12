import json
from django.http import JsonResponse
from games.models import GameScore
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"
class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"
class GameScoresView(TemplateView):
    template_name = "games/game-scores.html"
    def get_context_data(self, **kwargs):
        username = self.request.user.username
        context = super(GameScoresView, self).get_context_data(**kwargs)
        math_facts_scores =  GameScore.objects.filter(game__exact='MATH', user_name__exact=username).order_by('-created')
        p = Paginator(math_facts_scores, 5)
        page_number = self.request.GET.get('math_page')
        try:
            math_obj = p.get_page(page_number)
        except PageNotAnInteger:
            math_obj = p.page(1)
        except EmptyPage:
            math_obj = p.page(p.num_pages)
        context['math_obj'] = math_obj
        anagram_hunt_scores =  GameScore.objects.filter(game__exact='ANAGRAM', user_name__exact=username).order_by('-created')
        p = Paginator(anagram_hunt_scores, 5)
        page_number = self.request.GET.get('anagram_page')
        try:
            anagram_obj = p.get_page(page_number)
        except PageNotAnInteger:
            anagram_obj = p.page(1)
        except EmptyPage:
            anagram_obj = p.page(p.num_pages)
        context['anagram_obj'] = anagram_obj

        return context

class LeaderBoardsView(TemplateView):
    template_name = "games/leader-boards.html"

    def get_context_data(self, **kwargs):
        context = super(LeaderBoardsView, self).get_context_data(**kwargs)

        math_facts_scores =  GameScore.objects.filter(game__exact='MATH').order_by('-score')
        p = Paginator(math_facts_scores, 10)
        page_number = self.request.GET.get('math_page')
        try:
            math_obj = p.get_page(page_number)
        except PageNotAnInteger:
            math_obj = p.page(1)
        except EmptyPage:
            math_obj = p.page(p.num_pages)
        context['math_obj'] = math_obj

        anagram_hunt_scores =  GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        p = Paginator(anagram_hunt_scores, 10)
        page_number = self.request.GET.get('anagram_page')
        try:
            anagram_obj = p.get_page(page_number)
        except PageNotAnInteger:
            anagram_obj = p.page(1)
        except EmptyPage:
            anagram_obj = p.page(p.num_pages)
        context['anagram_obj'] = anagram_obj
        return context
def record_score(request):
    if request.user.username:
        data = json.loads(request.body)
        user_name = request.user.username
        game = data["game"]
        settings = data["settings"]
        score = data["score"]
        new_score = GameScore(user_name=user_name, game=game, settings=settings, score=score)
        new_score.save()
        response = {
            "success": True
        }
        return JsonResponse(response)
    
    return JsonResponse({
        "message": "You need to be logged in.",
        "success": False
    })