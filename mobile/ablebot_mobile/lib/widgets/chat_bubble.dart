import 'package:flutter/material.dart';
import '../models/chat_message.dart';

class ChatBubble extends StatelessWidget {
  final ChatMessage chatMessage;

  const ChatBubble({
    super.key,
    required this.chatMessage,
  });

  @override
  Widget build(BuildContext context) {
    final isUser = chatMessage.isUser;

    return Align(
      alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.symmetric(vertical: 6),
        padding: const EdgeInsets.all(14),
        constraints: const BoxConstraints(maxWidth: 300),
        decoration: BoxDecoration(
          color: isUser ? Colors.green.shade100 : Colors.grey.shade200,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Text(
          chatMessage.message,
          style: const TextStyle(fontSize: 16),
        ),
      ),
    );
  }
}