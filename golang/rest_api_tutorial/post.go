package main

import (
	"encoding/json"
	"fmt"
	"log"
	"napping"
	"net/http"
)

func post(url string) {
	s := napping.Session{}
	h :=  &http.Header{}
	h.Set("X-Custom-Header", "myvalue")
	s.Header = h

	var jsonStr = []byte(`{
			"ID": "3",
			"Title": "Newly Created Post",
			"desc": "The description for my new post",
			"content": "my article content"
		}`)

	var data map[string]json.RawMessage
	err := json.Unmarshal(jsonStr, &data)
	if err != nil {
		fmt.Println(err)
	}

	resp, err := s.Post(url, &data, nil, nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("response Status:", resp.Status())
	fmt.Println("response Headers:", resp.HttpResponse().Header)
	fmt.Println("response Body:", resp.RawText())
}

func api_delete(url string) {
	s := napping.Session{}
	h :=  &http.Header{}
	h.Set("X-Custom-Header", "myvalue")
	s.Header = h

	resp, err := s.Delete(url, nil, nil, nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("response Status:", resp.Status())
	fmt.Println("response Headers:", resp.HttpResponse().Header)
	fmt.Println("response Body:", resp.RawText())
}

func put(url string) {
	s := napping.Session{}
	h :=  &http.Header{}
	h.Set("X-Custom-Header", "myvalue")
	s.Header = h

	var jsonStr = []byte(`{
			"ID": "2",
			"Title": "Updated Post",
			"desc": "The description for my updated post",
			"content": "my updated article content"
		}`)

	var data map[string]json.RawMessage
	err := json.Unmarshal(jsonStr, &data)
	if err != nil {
		fmt.Println(err)
	}

	resp, err := s.Put(url, &data, nil, nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("response Status:", resp.Status())
	fmt.Println("response Headers:", resp.HttpResponse().Header)
	fmt.Println("response Body:", resp.RawText())
}

func main() {
	url := "http://localhost:10000/article/2"
	fmt.Println("URL:>", url)

	put(url)

}
