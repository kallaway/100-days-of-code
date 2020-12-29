import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:klotski_flutter/board/game_board.dart';

void main() {
  testWidgets('game board view test', (WidgetTester tester) async {
    // Build app and trigger a frame.
    await tester.pumpWidget(MyApp());
  });
}
