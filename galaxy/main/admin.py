# (c) 2012-2016, Ansible by Red Hat
#
# This file is part of Ansible Galaxy
#
# Ansible Galaxy is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by
# the Apache Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Ansible Galaxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Apache License for more details.
#
# You should have received a copy of the Apache License
# along with Galaxy.  If not, see <http://www.apache.org/licenses/>.

from django.contrib import admin
from galaxy.main.models import Platform, Role, RoleVersion

###################################################################################
# Admin Models


class PlatformAdmin(admin.ModelAdmin):
    pass


class RoleAdmin(admin.ModelAdmin):
    pass


class RoleVersionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(RoleVersion, RoleVersionAdmin)

# class RoleImportAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(RoleImport, RoleImportAdmin)

# class RoleRatingAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(RoleRating, RoleRatingAdmin)

# class CategoryAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(Category, CategoryAdmin)

# class UserAliasAdmin(admin.ModelAdmin):
#    pass
# admin.site.register(UserAlias, UserAliasAdmin)
