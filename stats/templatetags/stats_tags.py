from django import template

register = template.Library()


@register.filter(name="list_index")
def list_index(big_list, index):
    return big_list[int(index)]
