Middlwares add extra functionalities to the Redux dispatch function.

---

action --- (dispatched) --> middlewares ---> reducers.

Note that action can be anything that is about to touch the store through reducers:
- It could be redux actions
- It could be functions (redux-thunk middleware)
- It could be anything, as long as the middleware you're about to write to to handle it.

---

```javascript
const middleware = store => next => action => {
  // Before action touch reducers.
  
  let result = next(action);
  
  // After action touch reducers (and modify the store).
  
  return result;
}
```

