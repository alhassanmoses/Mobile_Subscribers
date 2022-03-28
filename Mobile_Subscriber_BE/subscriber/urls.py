from django.urls import path
from subscriber.views.MobileSubscriber import (CreateMobileSubscriberAPI,
                                               RetrieveMobSubAPI,
                                               ListMobileSubscriberAPI,
                                               ListMobSubNumbersAPI,
                                               UpdateMobileSubscriberAPI,
                                               DeleteMobileSubscriberAPI)

urlpatterns = [

    path
    (
        "create",
        CreateMobileSubscriberAPI.as_view(),
        name='create_sub'
    ),

    path
    (
        "list",
        ListMobileSubscriberAPI.as_view(),
        name='List_subs'
    ),

    path
    (
        "numbers/list",
        ListMobSubNumbersAPI.as_view(),
        name='List_sub_numbs'
    ),

    path
    (
        "<pk>",
        RetrieveMobSubAPI.as_view(),
        name='get_sub'
    ),

    path
    (
        "<pk>/update",
        UpdateMobileSubscriberAPI.as_view(),
        name='update_sub'
    ),

    path
    (
        "<pk>/delete",
        DeleteMobileSubscriberAPI.as_view(),
        name='delete_sub'
    ),
]
