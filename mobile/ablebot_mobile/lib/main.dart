import 'package:flutter/material.dart';
import 'screens/chat_screen.dart';

void main() {
  runApp(const AbleBotApp());
}

class AbleBotApp extends StatelessWidget {
  const AbleBotApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AbleBot',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorSchemeSeed: Colors.green,
        useMaterial3: true,
      ),
      home: const ChatScreen(),
    );
  }
}

