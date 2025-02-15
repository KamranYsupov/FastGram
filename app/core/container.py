from dependency_injector import containers, providers

from app.repositories import (
    RepositoryUser,
    RepositoryRefreshToken,
)
from app.services import (
    UserService,
    JWTService,
)
from app.db import (
    DataBaseManager,
    User,
    RefreshToken,
)
from app.core.config import settings




class Container(containers.DeclarativeContainer):
    db_manager = providers.Singleton(DataBaseManager, db_url=settings.db_url)
    session = providers.Resource(db_manager().get_async_session)

    # region repository
    repository_user = providers.Singleton(
        RepositoryUser, model=User, session=session
    )
    repository_refresh_token = providers.Singleton(
        RepositoryRefreshToken, model=RefreshToken, session=session
    )
    # endregion

    # region services
    user_service = providers.Singleton(
        UserService, 
        repository_user=repository_user, 
        unique_fields=('username', 'email')
    )
    jwt_service = providers.Singleton(
        JWTService, repository_refresh_token=repository_refresh_token
    )
    # endregion


container = Container()
container.init_resources()
container.wire(modules=settings.container_wiring_modules)
