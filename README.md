- Unix/Linux commands.
- REST
- Git
- Regex
- Python

---

Read articles:

- [Dashes vs. Underscores in URLs](https://writing.fletom.com/dashes_vs_underscores_in_URLs?fbclid=IwAR0k6BS-FbbaRpCKIX-khb9qZdWzxxVN7VvshRiIwOAXe9fKIOy6l0rhuc4)
  
  Use underscores, because dashes in English have their own meaning. `man-eating-shark` is a man-eating shark or a man eating shark meat?

- [What is REST](https://restfulapi.net/)
  
  Decouple client and server, cacheable, stateless.
  Resources = any information that can be named.
  Resource representation = state of resource at a timestamp, data format of resource representation = media-type.

- [Why HATEOAS is useless and what that means for REST](https://medium.com/@andreasreiser94/why-hateoas-is-useless-and-what-that-means-for-rest-a65194471bc8?fbclid=IwAR0StTDqWbaZvltEUgx0ynLM6B0X_03PlCGhZGwX8rYe3u_xyp57nNlUYRs)
  
  HATEOAS:
  - from root URI, user can navigate entire interface dynamically.
  - evolvability by creating a uniform interface.
    
  Problems:
  - clients won't navigate the API dynamically => need API specification.
  - API is versioned by numberring (`/v1/`) => loss evolvability
