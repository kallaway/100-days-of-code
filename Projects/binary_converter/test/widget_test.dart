import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:binary_converter/main.dart';

void main() {
  testWidgets('Test Initial App State', (WidgetTester tester) async {
    await tester.pumpWidget(MyApp());
    expect(find.text('Result: '), findsOneWidget);
  });

  testWidgets('Test Conversion', (WidgetTester tester) async {

    var intNumb = 2;
    var binary = intNumb.toRadixString(2);

    await tester.pumpWidget(MyApp());
    await tester.enterText(find.byType(TextField), '2');
    await tester.tap(find.byType(FlatButton));
    await tester.pump();

    expect(find.text('Result: $binary'), findsOneWidget);
  });
}
