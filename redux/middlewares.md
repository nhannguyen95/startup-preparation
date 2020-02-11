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

---

It is okay to use Symbols, Promises, or other non-serializable values in an action if the action is intended for use by middleware. Actions only need to be serializable by the time they actually reach the store and are passed to the reducers.
