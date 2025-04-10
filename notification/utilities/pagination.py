from rest_framework.pagination import PageNumberPagination


#create a pagination obj
class myPageNumberPagination(PageNumberPagination):
    page_size=50
    page_query_param='page'
    page_size_query_param='size'
    max_page_size=500