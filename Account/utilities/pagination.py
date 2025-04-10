from rest_framework.pagination  import PageNumberPagination


class userPagination(PageNumberPagination):
    page_size=20
    page_query_param='page'
    max_page_size=500
    page_size_query_param='page_size'