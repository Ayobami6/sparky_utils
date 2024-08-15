---
description: Use service response to have consistent API response for all your Rest API
---

# 🔬 API Response

{% code title="views.py" fullWidth="true" %}
```python

from sparky_utils.response import service_response

def retrieve(self, request, *args, **kwargs):
        """Product retrieve get handler"""
        try:
            assets_fields: List[str] = ["name", "image", "alt"]
            # get product
            product = self.get_object()
            # get product assets
            assets = ProductAssets.objects.only(*assets_fields).filter(product=product)
            serializer = ProductSerializer(
                product, context={"assets": assets, "request": request}
            )
            return service_response(
                status="success",
                message="Product retrieved successfully",
                data=serializer.data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()
```
{% endcode %}



```json
{
    "status": "success",
    "message": "Product retrieved successfully",
    "data": {
        "id": "538ba39e-aee4-4daf-ac74-0d60f110c7bd",
        "assets": [
            {
                "name": "s1",
                "image": "http://localhost:8000/media/product_assests/s1.jpeg",
                "alt": "s1"
            },
            {
                "name": "s2",
                "image": "http://localhost:8000/media/product_assests/s2.jpeg",
                "alt": "sd"
            }
        ],
        "groups_link": "http://localhost:8000/products",
        "self_link": "http://localhost:8000/products/538ba39e-aee4-4daf-ac74-0d60f110c7bd",
        "name": "Thick Platform Pillow Bathroom Home Slippers",
        "price": "3000.00",
        "description": "<p><strong>&bull; Thick Platform Design :</strong>The thick platform design of these slippers provides extra comfort and support, making them ideal for indoor use during the summer season.</p>\r\n\r\n<p>&nbsp;</p>sizes larger when purchasing.</p>",
        "views": 0,
        "discount_price": "2499.98",
        "created_at": "2024-08-14T21:39:31",
        "updated_at": "2024-08-14T21:39:31",
        "category": 2
    }
}
```
