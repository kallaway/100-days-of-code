import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Binary Converter',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Binary Converter'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  TextEditingController _valueController = new TextEditingController();
  var _binary = "";

  void _convertToBinary() {
    var strToInt = int.parse(this._valueController.text);
    this._binary = strToInt.toRadixString(2);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: ListView(
        children: [
          Container(
            child: Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        child: TextField(
                          controller: _valueController,
                          decoration: InputDecoration(
                            hintText: 'Enter a number to convert'
                          )
                        )
                      )
                    ]
                  )
                ),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        child: FlatButton(
                          color: Colors.blue,
                          textColor: Colors.white,
                          disabledColor: Colors.grey,
                          disabledTextColor: Colors.black,
                          padding: EdgeInsets.all(8.0),
                          splashColor: Colors.blueAccent,
                          onPressed: () {
                            setState(() {
                              this._convertToBinary();
                            });},
                          child: Text(
                            "Convert",
                            style: TextStyle(fontSize: 20.0)
                          )
                        )
                      )
                    ]
                  )
                )
              ]
            )
          ),
          Container(
            child: Row(
              children: [
                Expanded(child: Text('Result: $_binary')),
              ],
            ),
          )
        ]
      )
    );
  }
}
