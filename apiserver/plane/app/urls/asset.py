from django.urls import path


from plane.app.views import (
    FileAssetEndpoint,
    UserAssetsEndpoint,
    FileAssetViewSet,
    # V2 Endpoints
    WorkspaceFileAssetEndpoint,
    UserAssetsV2Endpoint,
    StaticFileAssetEndpoint,
    AssetRestoreEndpoint,
)


urlpatterns = [
    path(
        "workspaces/<str:slug>/file-assets/",
        FileAssetEndpoint.as_view(),
        name="file-assets",
    ),
    path(
        "workspaces/file-assets/<uuid:workspace_id>/<str:asset_key>/",
        FileAssetEndpoint.as_view(),
        name="file-assets",
    ),
    path(
        "users/file-assets/",
        UserAssetsEndpoint.as_view(),
        name="user-file-assets",
    ),
    path(
        "users/file-assets/<str:asset_key>/",
        UserAssetsEndpoint.as_view(),
        name="user-file-assets",
    ),
    path(
        "workspaces/file-assets/<uuid:workspace_id>/<str:asset_key>/restore/",
        FileAssetViewSet.as_view(
            {
                "post": "restore",
            }
        ),
        name="file-assets-restore",
    ),
    # V2 Endpoints
    path(
        "assets/v2/workspaces/<str:slug>/",
        WorkspaceFileAssetEndpoint.as_view(),
        name="workspace-file-assets",
    ),
    path(
        "assets/v2/workspaces/<str:slug>/<uuid:asset_id>/",
        WorkspaceFileAssetEndpoint.as_view(),
        name="workspace-file-assets",
    ),
    path(
        "assets/v2/user-assets/",
        UserAssetsV2Endpoint.as_view(),
        name="user-file-assets",
    ),
    path(
        "assets/v2/user-assets/<uuid:asset_id>/",
        UserAssetsV2Endpoint.as_view(),
        name="user-file-assets",
    ),
    path(
        "assets/v2/<uuid:asset_id>/restore/",
        AssetRestoreEndpoint.as_view(),
        name="asset-restore",
    ),
    path(
        "assets/v2/static/<uuid:asset_id>/",
        StaticFileAssetEndpoint.as_view(),
        name="static-file-asset",
    ),
]
