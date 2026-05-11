import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../models/chat_message.dart';
import '../widgets/chat_bubble.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController _controller = TextEditingController();

  String _selectedMode = 'rule-based';
  final List<ChatMessage> _messages = [];
  bool _isLoading = false;

  final List<String> _modes = [
    'rule-based',
    'bert',
    'bert-ft',
  ];

  Future<void> _sendMessage() async {
    final message = _controller.text.trim();
    final userMessage = message;

    if (message.isEmpty) return;

    setState(() {
      _isLoading = true;

      _messages.add(
        ChatMessage(
          message: userMessage,
          isUser: true,
        ),
      );
    });

    try {
      final result = await ApiService.sendChatMessage(
        message: message,
        mode: _selectedMode,
      );

      final botReply =
        result['response']?.toString() ??
        result['reply']?.toString() ??
        result['answer']?.toString() ??
        result.toString();

    setState(() {
      _messages.add(
        ChatMessage(
          message: botReply,
          isUser: false,
        ),
      );
    });

      _controller.clear();
    } catch (e) {
      setState(() {
        _messages.add(
          ChatMessage(
            message: 'Unable to connect to AbleBot backend. Error: $e',
            isUser: false,
          ),
        );
      });
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('AbleBot Mobile'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            DropdownButtonFormField<String>(
              value: _selectedMode,
              decoration: const InputDecoration(
                labelText: 'AI Mode',
                border: OutlineInputBorder(),
              ),
              items: _modes.map((mode) {
                return DropdownMenuItem(
                  value: mode,
                  child: Text(mode),
                );
              }).toList(),
              onChanged: (value) {
                if (value != null) {
                  setState(() {
                    _selectedMode = value;
                  });
                }
              },
            ),
            const SizedBox(height: 16),
            TextField(
              controller: _controller,
              minLines: 1,
              maxLines: 4,
              decoration: const InputDecoration(
                labelText: 'Ask AbleBot',
                hintText: 'Example: How can I apply for a PWD ID?',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),
            SizedBox(
              width: double.infinity,
              height: 52,
              child: ElevatedButton.icon(
                onPressed: _isLoading ? null : _sendMessage,
                icon: const Icon(Icons.send),
                label: Text(_isLoading ? 'Sending...' : 'Send'),
              ),
            ),
            const SizedBox(height: 24),
            Expanded(
              child: ListView.builder(
                itemCount: _messages.length,
                itemBuilder: (context, index) {
                  return ChatBubble(
                    chatMessage: _messages[index],
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}