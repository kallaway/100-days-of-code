"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/api/rpc/getCurrentUser";
exports.ids = ["pages/api/rpc/getCurrentUser"];
exports.modules = {

/***/ "./app/users/queries/getCurrentUser.ts":
/*!*********************************************!*\
  !*** ./app/users/queries/getCurrentUser.ts ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var next_data_client__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/data-client */ \"next/data-client\");\n/* harmony import */ var next_data_client__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(next_data_client__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var db__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! db */ \"./db/index.ts\");\n\n\n\nasync function getCurrentUser(_ = null, {\n  session\n}) {\n  if (!session.userId) return null;\n  const user = await db__WEBPACK_IMPORTED_MODULE_1__.default.user.findFirst({\n    where: {\n      id: session.userId\n    },\n    select: {\n      id: true,\n      name: true,\n      email: true,\n      role: true\n    }\n  });\n  return user;\n}\n\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ((0,next_data_client__WEBPACK_IMPORTED_MODULE_0__.buildRpcResolver)(getCurrentUser, {\n  \"resolverName\": \"getCurrentUser\",\n  \"resolverType\": \"query\",\n  \"routePath\": \"/api/rpc/getCurrentUser\"\n}));//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9hcHAvdXNlcnMvcXVlcmllcy9nZXRDdXJyZW50VXNlci50cy5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7OztBQUNBOztBQUVlLGVBQWVDLGNBQWYsQ0FBOEJDLENBQUMsR0FBRyxJQUFsQyxFQUF3QztBQUFFQyxFQUFBQTtBQUFGLENBQXhDLEVBQTBEO0FBQ3ZFLE1BQUksQ0FBQ0EsT0FBTyxDQUFDQyxNQUFiLEVBQXFCLE9BQU8sSUFBUDtBQUVyQixRQUFNQyxJQUFJLEdBQUcsTUFBTUwsc0RBQUEsQ0FBa0I7QUFDbkNPLElBQUFBLEtBQUssRUFBRTtBQUFFQyxNQUFBQSxFQUFFLEVBQUVMLE9BQU8sQ0FBQ0M7QUFBZCxLQUQ0QjtBQUVuQ0ssSUFBQUEsTUFBTSxFQUFFO0FBQUVELE1BQUFBLEVBQUUsRUFBRSxJQUFOO0FBQVlFLE1BQUFBLElBQUksRUFBRSxJQUFsQjtBQUF3QkMsTUFBQUEsS0FBSyxFQUFFLElBQS9CO0FBQXFDQyxNQUFBQSxJQUFJLEVBQUU7QUFBM0M7QUFGMkIsR0FBbEIsQ0FBbkI7QUFLQSxTQUFPUCxJQUFQO0FBQ0Q7O0FBVEQsaUVBQWUsbUVBQWVKLGNBQTlCO0FBQUE7QUFBQTtBQUFBO0FBQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9ibGl0ei10ZXN0cy8uL2FwcC91c2Vycy9xdWVyaWVzL2dldEN1cnJlbnRVc2VyLnRzPzcyNTYiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgQ3R4IH0gZnJvbSBcImJsaXR6XCJcbmltcG9ydCBkYiBmcm9tIFwiZGJcIlxuXG5leHBvcnQgZGVmYXVsdCBhc3luYyBmdW5jdGlvbiBnZXRDdXJyZW50VXNlcihfID0gbnVsbCwgeyBzZXNzaW9uIH06IEN0eCkge1xuICBpZiAoIXNlc3Npb24udXNlcklkKSByZXR1cm4gbnVsbFxuXG4gIGNvbnN0IHVzZXIgPSBhd2FpdCBkYi51c2VyLmZpbmRGaXJzdCh7XG4gICAgd2hlcmU6IHsgaWQ6IHNlc3Npb24udXNlcklkIH0sXG4gICAgc2VsZWN0OiB7IGlkOiB0cnVlLCBuYW1lOiB0cnVlLCBlbWFpbDogdHJ1ZSwgcm9sZTogdHJ1ZSB9LFxuICB9KVxuXG4gIHJldHVybiB1c2VyXG59XG4iXSwibmFtZXMiOlsiZGIiLCJnZXRDdXJyZW50VXNlciIsIl8iLCJzZXNzaW9uIiwidXNlcklkIiwidXNlciIsImZpbmRGaXJzdCIsIndoZXJlIiwiaWQiLCJzZWxlY3QiLCJuYW1lIiwiZW1haWwiLCJyb2xlIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./app/users/queries/getCurrentUser.ts\n");

/***/ }),

/***/ "./db/index.ts":
/*!*********************!*\
  !*** ./db/index.ts ***!
  \*********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var next_stdlib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/stdlib */ \"next/stdlib\");\n/* harmony import */ var next_stdlib__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(next_stdlib__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _prisma_client__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @prisma/client */ \"@prisma/client\");\n/* harmony import */ var _prisma_client__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_prisma_client__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony reexport (unknown) */ var __WEBPACK_REEXPORT_OBJECT__ = {};\n/* harmony reexport (unknown) */ for(const __WEBPACK_IMPORT_KEY__ in _prisma_client__WEBPACK_IMPORTED_MODULE_1__) if(__WEBPACK_IMPORT_KEY__ !== \"default\") __WEBPACK_REEXPORT_OBJECT__[__WEBPACK_IMPORT_KEY__] = () => _prisma_client__WEBPACK_IMPORTED_MODULE_1__[__WEBPACK_IMPORT_KEY__]\n/* harmony reexport (unknown) */ __webpack_require__.d(__webpack_exports__, __WEBPACK_REEXPORT_OBJECT__);\n\n\nconst EnhancedPrisma = (0,next_stdlib__WEBPACK_IMPORTED_MODULE_0__.enhancePrisma)(_prisma_client__WEBPACK_IMPORTED_MODULE_1__.PrismaClient);\n\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (new EnhancedPrisma());//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9kYi9pbmRleC50cy5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7OztBQUFBO0FBQ0E7QUFFQSxNQUFNRSxjQUFjLEdBQUdGLDBEQUFhLENBQUNDLHdEQUFELENBQXBDO0FBRUE7QUFDQSxpRUFBZSxJQUFJQyxjQUFKLEVBQWYiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9ibGl0ei10ZXN0cy8uL2RiL2luZGV4LnRzP2ZiNTQiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgZW5oYW5jZVByaXNtYSB9IGZyb20gXCJibGl0elwiXG5pbXBvcnQgeyBQcmlzbWFDbGllbnQgfSBmcm9tIFwiQHByaXNtYS9jbGllbnRcIlxuXG5jb25zdCBFbmhhbmNlZFByaXNtYSA9IGVuaGFuY2VQcmlzbWEoUHJpc21hQ2xpZW50KVxuXG5leHBvcnQgKiBmcm9tIFwiQHByaXNtYS9jbGllbnRcIlxuZXhwb3J0IGRlZmF1bHQgbmV3IEVuaGFuY2VkUHJpc21hKClcbiJdLCJuYW1lcyI6WyJlbmhhbmNlUHJpc21hIiwiUHJpc21hQ2xpZW50IiwiRW5oYW5jZWRQcmlzbWEiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./db/index.ts\n");

/***/ }),

/***/ "@prisma/client":
/*!*********************************!*\
  !*** external "@prisma/client" ***!
  \*********************************/
/***/ ((module) => {

module.exports = require("@prisma/client");

/***/ }),

/***/ "next/data-client":
/*!***********************************!*\
  !*** external "next/data-client" ***!
  \***********************************/
/***/ ((module) => {

module.exports = require("next/data-client");

/***/ }),

/***/ "next/stdlib":
/*!******************************!*\
  !*** external "next/stdlib" ***!
  \******************************/
/***/ ((module) => {

module.exports = require("next/stdlib");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("./app/users/queries/getCurrentUser.ts"));
module.exports = __webpack_exports__;

})();