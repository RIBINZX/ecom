# myapp/templatetags/custom_filters.py
from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def star_rating(value):
    full_stars = int(value)
    half_star = (value % 1) >= 0.5
    empty_stars = 5 - full_stars - half_star

    stars_html = ""

    for _ in range(full_stars):
        stars_html += '<i class="fas fa-star"></i>'
    if half_star:
        stars_html += '<i class="fas fa-star-half-alt"></i>'
    for _ in range(empty_stars):
        stars_html += '<i class="far fa-star"></i>'

    return format_html(stars_html)
