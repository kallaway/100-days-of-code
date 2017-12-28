<?php

function checkInternalAccess(string $email) {
    if (($at = strpos($email, "@")) > 0) {
        if ($domain = trim(substr($email, $at + 1))) {
            return $domain === "yactf.ru";
        }
    }
    return false;
}

function sign($email) {
    return hash_hmac("md5", $email, getenv("SECRET_KEY") || "dev-key");
}

function unsignEmail() {
    $signed = $_COOKIE["wifikeeper_email"]?: null;
    if ($signed === null) {
        return '';
    }

    list($email, $sign) = explode(":", $signed, 2);
    if (hash_equals($sign, sign($email))) {
        return $email;
    }
    return '';
}  

function signEmail(string $email) {
    $sign = sign($email);
    setcookie("wifikeeper_email", "${email}:${sign}", time()+60*60*24*30);
}