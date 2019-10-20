from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ allow user edit their own profile """

    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to edit ther own profile """
        if request.method in permissions.SAFE_METHODS: # if the request is GET
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ allow user edit their own status texts """

    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to edit ther own profile """
        if request.method in permissions.SAFE_METHODS: # if the request is GET
            return True

        return obj.user_profile.id == request.user.id
