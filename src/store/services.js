import axios from "axios"
import {
  PARENT_ONLY_USERNAME,
  PARENT_ONLY_PASSWORD,
  REGISTER_USERNAME,
  REGISTER_PASSWORD
} from "react-native-dotenv"
const parentOnly = axios.create({
  baseURL:
    "https://app.jackrabbitclass.com/jr3.0/ParentPortal/Login?orgID=540191",
  auth: { username: PARENT_ONLY_USERNAME, password: PARENT_ONLY_PASSWORD },
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
const register = axios.create({
  baseURL: "https://app3.jackrabbitclass.com/regv2.asp?id=540191",
  auth: { username: REGISTER_USERNAME, password: REGISTER_PASSWORD },
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
export const apiService = {}
