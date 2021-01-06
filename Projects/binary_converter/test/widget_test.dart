import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:binary_converter/main.dart';

void main() {
  testWidgets('Test Initial App State', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(MyApp());
    final resultTextKey = Key('resultText');
    expect(find.byKey(resultTextKey), findsOneWidget);
  });
}
