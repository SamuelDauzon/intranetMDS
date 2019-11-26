from django.contrib import admin

from .models import CallCategory, CallTag, Call, UrlSite

class CallAdmin(admin.ModelAdmin):
    list_display = ('created', 'customer', 'teammember', 'solved', 'title', )
    list_filter = ['solved', 'teammember', 'tags']
    list_editable = ['solved', 'teammember', ]
    search_fields = ['customer', 'teammember', 'title', ]

class UrlSiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'available', )

admin.site.register(CallCategory)
admin.site.register(CallTag)
admin.site.register(Call, CallAdmin)
admin.site.register(UrlSite, UrlSiteAdmin)


