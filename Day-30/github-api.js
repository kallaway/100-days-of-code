require('dotenv').config();
const express = require('express');


const request = require('request');

const app = express();
console.log(process.env.github_client_id);

var config = {
   client_id: process.env.github_client_id,
   client_secret: process.env.github_client_secret,
   redirect_url: 'http://localhost:3000/github/callback',
   authorize_url:'https://github.com/login/oauth/authorize',
   token_url: 'https://github.com/login/oauth/access_token',
   user_url: 'https://api.github.com/user',
   scope: 'user'
 };

app.get('/github/auth', function(req,res){
   // redirect the user to github authorization url
   return res.redirect(config.authorize_url);
});

app.get('/github/callback', function(req,res){
   // extract authorize code 
   var code = req.query.code

   // configure request params
   options = {
     method: 'POST',
     uri: config.token_url,   
     formData: {
       client_id   : config.client_id,
       client_secret   : config.client_secret,
       code : code
     },
     headers: {
       accept:  'application/json'
     }
   };

   // make a request for auth_token using above options
   request(options , function(e,r,b){
   
     // process the body
     if(b) {
       jb = JSON.parse(b)

       // configure request to fetch user information
       options_user = {
         method:'GET',
         url: config.user_url+'?access_token='+jb.access_token,
         headers: {
           accept: 'application/json',
           'User-Agent': 'custom'
         }
       }
       request(options_user , function(ee,rr,bb){
         // process the body
         if(bb) {
           var bo = JSON.parse(bb)
           var resp = {
             name: bo.name ,
             url: bo.url ,
             id: bo.id ,
             bio: bo.bio
           }
           return res.json(resp)
         }
         else {
           console.log(er)
           return res.json(er)
         }
       });
     }
   });
 });


// Section 4 start the app

app.listen(3000, () => console.log('Njera github-api app listening on port 3000!'));
