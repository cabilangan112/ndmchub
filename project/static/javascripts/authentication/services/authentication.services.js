/**
* Authentication
* @namespace thinkster.authentication.services
*/
(function () {
  'use strict';

  angular
    .module('thinkster.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http'];

  /**
  * @namespace Authentication
  * @returns {Factory}
  */
  function Authentication($cookies, $http) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
    var Authentication = {
      register: register
    };

    return Authentication;

    ////////////////////

    /**
    * @name register
    * @desc Try to register a new user
    * @param {string} username The username entered by the user
    * @param {string} password The password entered by the user
    * @param {string} email The email entered by the user
    * @returns {Promise}
    * @memberOf thinkster.authentication.services.Authentication
    */
    function register(email, password, username) {
      return $http.post('/api/v1/accounts/', {
        email: email
        password: password,
 
      });
    }

  }
  /**
 * @name login
 * @desc Try to log in with email `email` and password `password`
 * @param {string} email The email entered by the user
 * @param {string} password The password entered by the user
 * @returns {Promise}
 * @memberOf thinkster.authentication.services.Authentication
 */
function login(email, password) {
  return $http.post('/api/v1/auth/login/', {
    email: email, password: password
  });
}
/**
 * @name getAuthenticatedAccount
 * @desc Return the currently authenticated account
 * @returns {object|undefined} Account if authenticated, else `undefined`
 * @memberOf thinkster.authentication.services.Authentication
 */
function getAuthenticatedAccount() {
  if (!$cookies.authenticatedAccount) {
    return;
  }

  return JSON.parse($cookies.authenticatedAccount);
}
})();