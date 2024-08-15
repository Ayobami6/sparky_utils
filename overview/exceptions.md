---
icon: tire-pressure-warning
description: >-
  Handle your internal server error gracefully and log the exception for later
  reference
---

# Exceptions

{% code title="views.py" %}
```python
from sparky_utils.exceptions import handle_internal_server_exception

def get(self, request, *args, **kwargs) -> Any:
        try:
            # get all advert banners
            banners = AdvertBanner.objects.all().order_by("-updated_at")[:5]
            serializer = AdvertBannerSerializer(banners, many=True)
            return service_response(
                status="success",
                message="Advert banners retrieved successfully",
                data=serializer.data,
                status_code=200,
            )

        except Exception:
            return handle_internal_server_exception() # handle the exception
```
{% endcode %}
