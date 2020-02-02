action --- (dispatched) --> middlewares ---> reducers.

---

```javascript
const middleware = store => next => action => {
  // Before action touch reducers.
  
  let result = next(action);
  
  // After action touch reducers (and modify the store).
  
  return result;
}
```

