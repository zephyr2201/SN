from drf_yasg import openapi

date_from = openapi.Parameter(
    'date_from',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Example:2021-06-11'
)

date_to = openapi.Parameter(
    'date_to',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Example:2021-08-31'
)