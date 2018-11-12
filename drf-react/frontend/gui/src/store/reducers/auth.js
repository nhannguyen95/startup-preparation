import * as actionTypes from '../actions/actionTypes';
import { updateObject } from '../utility';

const initialState = {
  token: null,
  error: null,
  loading: false
}

// Redux reducer
const authStart = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: true
  });
}

// Redux reducer
const authSuccess = (state, action) => {
  return updateObject(state, {
    token: action.token,
    error: null,
    loading: false
  });
}

// Redux reducer
const authFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  });
}

// Redux reducer
const authLogout = (state, action) => {
  return updateObject(state, {
    token: null
  });
}

// Redux reducer
// Should be pure function:
// - No API calls
// - No suprises
// - No router transitions
// - The result should be predictable
const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.AUTH_START: return authStart(state, action);
    case actionTypes.AUTH_SUCCESS: return authSuccess(state, action);
    case actionTypes.AUTH_FAIL: return authFail(state, action);
    case actionTypes.AUTH_LOGOUT: return authLogout(state, action);
    default:
      return state;
  }
}

export default reducer;