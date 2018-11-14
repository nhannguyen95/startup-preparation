This is the code for the tutorial https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/

What I learned: Django Rest Framework (DRF)

- DRF's generics views: ListCreateAPIView, RetrieveAPIView, etc.
- Adding permission for each API endpoint (per-view level) and object (per-object level).
- Adding pagination to limit the number of results per API endpoint, the response will have in addition `previous` and `next` keys.
- Adding relationships between entities (for example if you query for a user, the response also gives you the snippets he owns).
- Generating an API schema.