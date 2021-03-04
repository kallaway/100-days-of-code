package main

import (
	"fmt"
	"log"
	"net/http"
	"encoding/json"
	"mux"
	"io/ioutil"
)

type Article struct {
	Id string `json:"Id"`
	Title string `json:"Title"`
	Desc string `json:"desc"`
	Content string `json:"content"`
}

// let's declare a global Article array that we can then populate in our
// main function to simulate a database
var Articles []Article

func returnAllArticles(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: returnAllArticles")
	json.NewEncoder(w).Encode(Articles)
}

func returnSingleArticle(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	key := vars["id"]

	// loop over all of our articles and if article.Id equals the key passed
	// in then return the article encoded as JSON
	for _, article := range Articles {
		if article.Id == key {
			json.NewEncoder(w).Encode(article)
		}
	}
}

func createNewArticle(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: createNewArticle")
	// get the body of our POST request and return the string response
	// containing the request body
	reqBody, _ := ioutil.ReadAll(r.Body)
	var article Article
	json.Unmarshal(reqBody, &article)
	// update our global Articcles array to include our new article
	Articles = append(Articles, article)

	json.NewEncoder(w).Encode(article)
}

func deleteArticle(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: deleteArticle")
	// once again we will need to parse the path parameters
	vars := mux.Vars(r)
	// we will need to extract the 'id' of the article we wish to delete
	id := vars["id"]

	// we then need to loop through our articles
	for index, article := range Articles {
		// if our id path param matches one of our articles
		if article.Id == id {
			// updates our Articles array to remove the article
			Articles = append(Articles[:index], Articles[index+1:]...)
		}
	}
}

func updateArticle(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: updateArticle")
	// get the body of our POST request and return the string response
	// containing the request body
	reqBody, _ := ioutil.ReadAll(r.Body)
	var updated_article Article
	json.Unmarshal(reqBody, &updated_article)
	// Find the right article and update it
	vars := mux.Vars(r)
	id := vars["id"]
	for index, article := range Articles {
		// if our id path param matches one of our articles
		if article.Id == id {
			println("updating articles array")
			Articles[index] = updated_article
		}
	}

	json.NewEncoder(w).Encode(updated_article)
}

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the HomePage!")
	fmt.Println("Endpoint Hit: homepage")
}

func handleRequests() {
	// creates a new instance of a mux router
	myRouter := mux.NewRouter().StrictSlash(true)
	//replace http.HandleFunc with myRouter.HandleFunc
	myRouter.HandleFunc("/", homePage)
	// add our articles route and map it to our returnAllArticles function
	myRouter.HandleFunc("/all", returnAllArticles)
	// if the DELETE method isn't before the line below it, it won't work
	myRouter.HandleFunc("/article/{id}", deleteArticle).Methods("DELETE")
	myRouter.HandleFunc("/article/{id}", updateArticle).Methods("PUT")
	myRouter.HandleFunc("/article/{id}", returnSingleArticle)
	myRouter.HandleFunc("/article", createNewArticle).Methods("POST")
	log.Fatal(http.ListenAndServe(":10000", myRouter))
}

func main() {
	fmt.Println("Rest API v2.0 - Mux Routers")
	Articles = []Article{
		Article{Id: "1", Title: "Hello", Desc: "Article Description", Content: "Article Content"},
		Article{Id: "2", Title: "Hello 2", Desc: "Article Description", Content: "Article Content"},
	}
	handleRequests()
}
