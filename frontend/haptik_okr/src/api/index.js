import APIRequest from "./APIRequest";
const BASE_URL = "http://127.0.0.1:8000";

class API {
  constructor() {
    this.request = new APIRequest();
  }

  // CLASS SETTERS
  _setToken = token => this.request.setToken(token);
}
