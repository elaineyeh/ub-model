from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = "UB 醬"

admin_site = MyAdminSite(name='myadmin')
