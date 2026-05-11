import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://10.0.0.18:5000';

  static Future<Map<String, dynamic>> sendChatMessage({
    required String message,
    required String mode,
  }) async {
    final url = Uri.parse('$baseUrl/chat');

    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'message': message,
        'mode': mode,
      }),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to connect to AbleBot backend');
    }
  }
  static Future<bool> checkHealth() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/health'));
      return response.statusCode == 200;
    } catch (e) {
      return false;
    }
  }

}

