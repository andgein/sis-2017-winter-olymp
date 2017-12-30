from django.template.defaulttags import register


@register.filter
def get_item_or_empty(dictionary, key):
    return dictionary.get(key, '')


@register.filter
def get_item(dictionary, key):
    return dictionary[key]