from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('category-choices/', views.category_choices, name='category-choices'),
    path('',views.VideoListView.as_view(),name='videolist-view'),
    path('<int:pk>/',views.VideoView.as_view(),name='video-view'),
    
    path('watchlater/', views.WatchLaterListByUserAPIView.as_view(), name='watch-later-list'),
    path('watchlater/create/', views.WatchLaterCreateAPIView.as_view(), name='watch-later-create'),
    path('watchlater/remove/<int:video_id>/', views.WatchLaterDeleteAPIView.as_view(), name='watch-later-remove'),

    path('liked/', views.LikedListByUserAPIView.as_view(), name='liked-list'),
    path('liked/create/', views.LikedCreateAPIView.as_view(), name='liked-create'),
    path('liked/remove/<int:video_id>/', views.LikedDeleteAPIView.as_view(), name='liked-remove'),
    
    path('history/', views.HistoryListByUserAPIView.as_view(), name='history-list'),
    path('history/create/', views.HistoryCreateAPIView.as_view(), name='history-create'),
    path('history/remove/<int:video_id>/', views.HistoryDeleteAPIView.as_view(), name='history-remove'),
    path('history/clear/', views.HistoryClearByUserAPIView.as_view(), name='history-clear-by-user'),

    path('playlist/', views.playlist_list_by_user, name='playlist-list'),
    path('playlist/create/', views.PlaylistCreateAPIView.as_view(), name='playlist-create'),
    path('playlist/delete/<int:playlist_id>/', views.PlaylistDeleteAPIView.as_view(), name='playlist-delete'),
    path('playlist/<int:playlist_id>/videos/', views.playlist_videos, name='playlist-videos'),
    path('playlist/<int:playlist_id>/add/<int:video_id>/', views.add_video_to_playlist, name='add-video-to-playlist'),
    path('playlist/<int:playlist_id>/remove/<int:video_id>/', views.remove_video_from_playlist, name='remove-video-from-playlist'),
    path('playlist/check/<int:video_id>/', views.video_presence_in_playlists, name='video-presence-in-playlists'),

    path('liked/check/<int:video_id>/', views.is_video_liked, name='video-presence-in-like'),
    path('watchlater/check/<int:video_id>/', views.is_video_in_watch_later, name='video-presence-in-watchlater'),


    path('comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-detail'),
    path('comments/video/<int:video_id>/', views.nested_comments_by_video, name='nested-comments-by-video'),
]