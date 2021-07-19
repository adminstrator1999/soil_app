from django.contrib import admin

from main.models import File, History, Employee, News, HistoryImages, NewsImage, Contact, Document, DocumentImages, \
    GalleryType, Gallery, Laboratory, LaboratoryImage, Partner, Service, ServiceImages, Function


class HistoryImagesAdmin(admin.TabularInline):
    model = HistoryImages
    fk_name = 'history'
    autocomplete_fields = ('image',)


class HistoryAdmin(admin.ModelAdmin):
    inlines = [HistoryImagesAdmin, ]
    list_display = ('text', )


class NewsImageAdmin(admin.TabularInline):
    model = NewsImage
    fk_name = 'news'
    autocomplete_fields = ('image',)


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin, ]
    list_display = ('title', 'short_description')
    readonly_fields = ('view_count', )


class FileAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', ]


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number']


class DocumentImageAdmin(admin.TabularInline):
    model = DocumentImages
    fk_name = 'document'
    autocomplete_fields = ('image',)


class DocumentAdmin(admin.ModelAdmin):
    inlines = [DocumentImageAdmin, ]
    list_display = ['name', 'link1', 'link2']


class GalleryTypeAdmin(admin.ModelAdmin):
    list_display = ('title', )


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('type', )


class LaboratoryImageAdmin(admin.TabularInline):
    model = LaboratoryImage
    fk_name = 'laboratory'
    autocomplete_fields = ('image',)


class LaboratoryAdmin(admin.ModelAdmin):
    inlines = [LaboratoryImageAdmin, ]
    list_display = ('name', )


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ServiceImageAdmin(admin.TabularInline):
    model = ServiceImages
    fk_name = 'service'
    autocomplete_fields = ('image',)


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageAdmin, ]
    list_display = ('name', )


class FunctionAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(File, FileAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(GalleryType, GalleryTypeAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Function, FunctionAdmin)
