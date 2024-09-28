export const isAuthenticated = () => {
  return localStorage.getItem('token') === 'this_is_a_working_token'
}