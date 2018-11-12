This is the code for the tutorial https://www.youtube.com/watch?v=uZgRbnIsgrA&list=PLLRM7ROnmA9FxCtnLoIHAs6hIkJyd1dEx

What I learned:
- React
- Redux:
  - All states are in a unique store.
  - Actions are plain object with action type and additional information, Action Creators are functions return Actions.
  - Reducers take 2 inputs: an Action and current state of the store, output: the next state of the store. Reducers are pure functions.
- React-Redux:
  - Instead of passing down the store as props so that (container) components can read and write to it, react-redux allows using <Provider> to provide the store only once.
  - If a (container) component wants to read from or write to the store, we just connect it with `mapStateToProps` and `mapDispatchToProps`. These functions return dictionaries that is the props dictionary of the connected component.
- Redux-Thunk:
  - Middleware of Redux, allows Action Creators to return functions (because these functions are delayed to execute until they are dispatched - they are called "thunks"). If Redux receives an action, it sends that action to reducers. If Redux receives a function, it executes that function.
- React-Router-Dom
- Authentication and Authorization with Django Rest Framework and React
