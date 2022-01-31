def user_changed(sender, instance, **kwargs):
    # import 写在函数里面避免循环依赖
    from accounts.services import UserServices
    UserServices.invalidate_user(instance.id)


def profile_changed(sender, instance, **kwargs):
    # import 写在函数里面避免循环依赖
    from accounts.services import UserServices
    UserServices.invalidate_profile(instance.user_id)
