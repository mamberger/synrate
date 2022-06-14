from django.contrib import admin

from .models import Offer, FAQ, OfferCategory, OfferSubcategory, TgUser, VkUser, SearchQuery, Banner


class VkUserAdmin(admin.ModelAdmin):
    list_display = ['from_id', 'a_data']
    search_fields = ['from_id', 'a_data']


class TgUserAdmin(admin.ModelAdmin):
    list_display = ['from_id', 'a_data']
    search_fields = ['from_id', 'a_data']


# @admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'organisation', 'offer_start_date', 'home', ]
    search_fields = ['name', 'organisation', 'offer_start_date', 'home_name',
                     'home_name', 'url', 'location', 'offer_type',
                     'offer_end_date', 'owner',
                     'ownercontact', 'offer_price', 'additional_data',
                     'category', 'created_at', 'from_id', 'short_cat', 'owner_id', ]

    def short_name(self, obj):
        return obj.name[:25]

    def home(self, obj):
        home, nice_home_name = obj.home_name, obj.home_name

        if home == "nelikvidi":
            nice_home_name = 'nelikvidi.com'
        if home == "onlinecontract":
            nice_home_name = 'onlinecontract.ru'
        if home == "tektorg":
            nice_home_name = 'tektorg.ru'
        if home == "tenderpro":
            nice_home_name = 'tender.pro'
        if home == "isource":
            nice_home_name = 'reserve.isource.ru'
        if home == "etpgpb":
            nice_home_name = 'etpgpb.ru'
        if home == "fabrikant":
            nice_home_name = 'fabrikant.ru'
        if home == "etp-activ":
            nice_home_name = 'etp-activ.ru'
        if home == "b2b-center":
            nice_home_name = 'b2b-center.ru'
        if home == "vk.com":
            nice_home_name = 'vk.com'

        return nice_home_name


# @admin.register(OfferCategory)
class OfferCategoryAdmin(admin.ModelAdmin):
    pass


# @admin.register(OfferSubcategory)
class OfferSubcategoryAdmin(admin.ModelAdmin):
    pass

class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ['phrase', 'slug', 'search_count', 'offers_count', 'is_active', ]
    list_filter = ['is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('phrase',)}
    ordering = ['phrase']
    fields = ['phrase', 'slug', 'is_active']
    search_fields = ['phrase']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['banner_type', 'is_active']

#
#
# @admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']


admin.site.register(OfferSubcategory, OfferSubcategoryAdmin)
admin.site.register(OfferCategory, OfferCategoryAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(TgUser, TgUserAdmin)
admin.site.register(VkUser, VkUserAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(SearchQuery, SearchQueryAdmin)
admin.site.register(Banner, BannerAdmin)