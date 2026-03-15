import React, { useState, useEffect } from 'react';
import styles from './ChatWidget.module.css';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hello! I am your Physical AI assistant. How can I help you with the Humanoid Robotics textbook today?' }
  ]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const [selectionCoords, setSelectionCoords] = useState({ x: 0, y: 0 });
  const [selectedText, setSelectedText] = useState('');

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSendMessage = async (customQuery = null, context = null) => {
    // Ensure query is a string and not a React event object
    let query = "";
    if (typeof customQuery === 'string') {
      query = customQuery;
    } else {
      query = inputText;
    }

    if (!query || query.trim() === '') return;

    const userMessage = { sender: 'user', text: query };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInputText('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          query: query,
          context: context || null
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Server error: ${response.status}`);
      }

      const data = await response.json();
      const botMessage = { sender: 'bot', text: data.answer || "Sorry, I couldn't generate an answer." };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { 
        sender: 'bot', 
        text: `Error: ${error.message}. Please ensure the backend is running at http://localhost:8000` 
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setIsLoading(false);
      setIsOpen(true);
    }
  };

  const handleAskAI = () => {
    if (selectedText) {
      handleSendMessage(`Explain this selection: "${selectedText}"`, selectedText);
      setSelectedText(''); // Clear selection after asking
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      handleSendMessage();
    }
  };

  useEffect(() => {
    const handleMouseUp = (event) => {
      // Small timeout to allow selection to complete
      setTimeout(() => {
        const selection = window.getSelection();
        const text = selection.toString().trim();
        
        if (text && text.length > 2) {
          const range = selection.getRangeAt(0);
          const rect = range.getBoundingClientRect();
          
          setSelectionCoords({
            x: rect.left + window.scrollX + (rect.width / 2),
            y: rect.top + window.scrollY - 40 // Position above the text
          });
          setSelectedText(text);
        } else {
          // Check if we clicked on the "Ask AI" button itself
          if (!event.target.closest(`.${styles.askAIButton}`)) {
            setSelectedText('');
          }
        }
      }, 0);
    };

    const handleMouseDown = (event) => {
      // Close the button when starting a new selection, unless clicking the button
      if (!event.target.closest(`.${styles.askAIButton}`)) {
        setSelectedText('');
      }
    };

    document.addEventListener('mouseup', handleMouseUp);
    document.addEventListener('mousedown', handleMouseDown);
    return () => {
      document.removeEventListener('mouseup', handleMouseUp);
      document.removeEventListener('mousedown', handleMouseDown);
    };
  }, []);


  return (
    <>
      {selectedText && (
        <button 
          className={styles.askAIButton}
          style={{ left: `${selectionCoords.x}px`, top: `${selectionCoords.y}px` }}
          onClick={handleAskAI}
        >
          ✨ Ask AI
        </button>
      )}

      <button className={styles.chatToggleButton} onClick={toggleChat}>
        {isOpen ? '❌' : '💬'}
      </button>

      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <h3>AI Chatbot</h3>
            <button onClick={toggleChat} className={styles.closeButton}>
              ❌
            </button>
          </div>
          <div className={styles.chatMessages}>
            {messages.map((msg, index) => (
              <div key={index} className={`${styles.message} ${styles[msg.sender]}`}>
                {msg.text}
              </div>
            ))}
            {isLoading && (
              <div className={`${styles.message} ${styles.bot} ${styles.typing}`}>
                <span></span>
                <span></span>
                <span></span>
              </div>
            )}
          </div>
          <div className={styles.chatInput}>
            <textarea
              value={inputText}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
              placeholder="Ask me anything about the book..."
              rows="1"
            />
            <button onClick={() => handleSendMessage()} disabled={isLoading}>
              Send
            </button>
          </div>
        </div>
      )}
    </>
  );
};

export default ChatWidget;
