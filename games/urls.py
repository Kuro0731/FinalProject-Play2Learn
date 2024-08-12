from django.urls import path

from games.views import MathFactsView, AnagramHuntView, GameScoresView, LeaderBoardsView, record_score

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('record-score/', record_score, name="record-score"),
    path('games/game-scores/', GameScoresView.as_view(), name='game-scores'),
    path('games/leader-boards/', LeaderBoardsView.as_view(), name='leader-boards'),
]