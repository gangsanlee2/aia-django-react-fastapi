/**
=========================================================
* Material Dashboard 2 React - v2.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

/** 
  All of the routes for the Material Dashboard 2 React are added here,
  You can add a new route, customize the routes and delete the routes here.

  Once you add a new route on this file it will be visible automatically on
  the Sidenav.

  For adding a new route you can follow the existing routes in the routes array.
  1. The `type` key with the `collapse` value is used for a route.
  2. The `type` key with the `title` value is used for a title inside the Sidenav. 
  3. The `type` key with the `divider` value is used for a divider between Sidenav items.
  4. The `name` key is used for the name of the route on the Sidenav.
  5. The `key` key is used for the key of the route (It will help you with the key prop inside a loop).
  6. The `icon` key is used for the icon of the route on the Sidenav, you have to add a node.
  7. The `collapse` key is used for making a collapsible item on the Sidenav that has other routes
  inside (nested routes), you need to pass the nested routes inside an array as a value for the `collapse` key.
  8. The `route` key is used to store the route location which is used for the react router.
  9. The `href` key is used to store the external links location.
  10. The `title` key is only for the item with the type of `title` and its used for the title text on the Sidenav.
  10. The `component` key is used to store the component of its route.
*/

// Material Dashboard 2 React layouts
import Dashboard from "layouts/dashboard";
import Tables from "layouts/tables";
import Billing from "layouts/billing";
import RTL from "layouts/rtl";
import Notifications from "layouts/notifications";
import Profile from "layouts/profile";
import SignIn from "layouts/authentication/sign-in";
import SignUp from "layouts/authentication/sign-up";

// my own files
import Counter from "layouts/myown/cmm/components/Counter";
import Schedule from "layouts/myown/cop/containers/Schedule";
import Login from "layouts/myown/uat/containers/Login";
import Stroke from "layouts/myown/blog/components/Stroke";
import IrisForm from "layouts/myown/shop/containers/IrisForm";
import FashionForm from "layouts/myown/dlearn/containers/FashionForm";
import Number from "layouts/myown/dlearn/components/Number";
import NaverMovie from "layouts/myown/webcrawler/conponents/NaverMovie";
import SamsungReport from "layouts/myown/nlp/components/SamsungReport";
import NaverMovieReview from "layouts/myown/nlp/components/NaverMovieReview";
import UserList from "layouts/myown/uat/containers/UserList";
import KoreanClassify from "layouts/myown/nlp/components/KoreanClassify";
import AiTrader from "layouts/myown/dlearn/components/AiTrader";

// @mui icons
import Icon from "@mui/material/Icon";

const routes = [
  {
    type: "collapse",
    name: "Dashboard",
    key: "dashboard",
    icon: <Icon fontSize="small">dashboard</Icon>,
    route: "/dashboard",
    component: <Dashboard />,
  },
  {
    type: "collapse",
    name: "Tables",
    key: "tables",
    icon: <Icon fontSize="small">table_view</Icon>,
    route: "/tables",
    component: <Tables />,
  },
  {
    type: "collapse",
    name: "Billing",
    key: "billing",
    icon: <Icon fontSize="small">receipt_long</Icon>,
    route: "/billing",
    component: <Billing />,
  },
  {
    type: "collapse",
    name: "RTL",
    key: "rtl",
    icon: <Icon fontSize="small">format_textdirection_r_to_l</Icon>,
    route: "/rtl",
    component: <RTL />,
  },
  {
    type: "collapse",
    name: "Notifications",
    key: "notifications",
    icon: <Icon fontSize="small">notifications</Icon>,
    route: "/notifications",
    component: <Notifications />,
  },
  {
    type: "collapse",
    name: "Profile",
    key: "profile",
    icon: <Icon fontSize="small">person</Icon>,
    route: "/profile",
    component: <Profile />,
  },
  {
    type: "collapse",
    name: "Sign In",
    key: "sign-in",
    icon: <Icon fontSize="small">login</Icon>,
    route: "/authentication/sign-in",
    component: <SignIn />,
  },
  {
    type: "collapse",
    name: "Sign Up",
    key: "sign-up",
    icon: <Icon fontSize="small">assignment</Icon>,
    route: "/authentication/sign-up",
    component: <SignUp />,
  },
  {
    type: "collapse",
    name: "Counter",
    key: "Counter",
    icon: <Icon fontSize="small">Counter</Icon>,
    route: "/counter",
    component: <Counter />,
  },
  {
    type: "collapse",
    name: "Schedule",
    key: "Schedule",
    icon: <Icon fontSize="small">Schedule</Icon>,
    route: "/todos/",
    component: <Schedule />,
  },
  {
    type: "collapse",
    name: "Login",
    key: "Login",
    icon: <Icon fontSize="small">Login</Icon>,
    route: "/login",
    component: <Login />,
  },
  {
    type: "collapse",
    name: "Stroke",
    key: "Stroke",
    icon: <Icon fontSize="small">Stroke</Icon>,
    route: "/stroke",
    component: <Stroke />,
  },
  {
    type: "collapse",
    name: "IrisForm",
    key: "IrisForm",
    icon: <Icon fontSize="small">IrisForm</Icon>,
    route: "/iris",
    component: <IrisForm />,
  },
  {
    type: "collapse",
    name: "FashionForm",
    key: "FashionForm",
    icon: <Icon fontSize="small">FashionForm</Icon>,
    route: "/fashion",
    component: <FashionForm />,
  },
  {
    type: "collapse",
    name: "Number",
    key: "Number",
    icon: <Icon fontSize="small">Number</Icon>,
    route: "/number",
    component: <Number />,
  },
  {
    type: "collapse",
    name: "NaverMovie",
    key: "NaverMovie",
    icon: <Icon fontSize="small">NaverMovie</Icon>,
    route: "/naver-movie",
    component: <NaverMovie />,
  },
  {
    type: "collapse",
    name: "SamsungReport",
    key: "SamsungReport",
    icon: <Icon fontSize="small">SamsungReport</Icon>,
    route: "/samsung-report",
    component: <SamsungReport />,
  },
  {
    type: "collapse",
    name: "NaverMovieReview",
    key: "NaverMovieReview",
    icon: <Icon fontSize="small">NaverMovieReview</Icon>,
    route: "/naver-movie-review",
    component: <NaverMovieReview />,
  },
  {
    type: "collapse",
    name: "UserList",
    key: "UserList",
    icon: <Icon fontSize="small">UserList</Icon>,
    route: "/user-list",
    component: <UserList />,
  },
  {
    type: "collapse",
    name: "KoreanClassify",
    key: "KoreanClassify",
    icon: <Icon fontSize="small">KoreanClassify</Icon>,
    route: "/korean-classify",
    component: <KoreanClassify />,
  },
  {
    type: "collapse",
    name: "AiTrader",
    key: "AiTrader",
    icon: <Icon fontSize="small">AiTrader</Icon>,
    route: "/aitrader",
    component: <AiTrader />,
  },
];

export default routes;
