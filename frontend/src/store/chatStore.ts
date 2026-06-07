import { create } from "zustand";
import type { ChatMessage, ChatSession } from "../types/chat";

interface ChatState {
  currentSessionId: number | null;
  sessions: ChatSession[];
  messages: ChatMessage[];
  isLoading: boolean; 
  error: string | null;
  
  // Session management
  createSession: (title?: string) => number;
setCurrentSession: (sessionId: number) => void;
setCurrentSessionId: (
  sessionId: number | null
) => void;
deleteSession: (sessionId: number) => void;
updateSessionTitle: (
  sessionId: number,
  title: string
) => void;

  // Message management
  addMessage: (msg: Omit<ChatMessage, "id" | "timestamp">) => void;
  updateMessage: (messageId: string, updates: Partial<ChatMessage>) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  clearMessages: () => void;
  setMessages: (
  messages: ChatMessage[]
) => void;
}
const generateId = () => Date.now().toString();

// Helper functions for Date serialization


export const useChatStore = create<ChatState>()(
    (set, get) => ({
      currentSessionId: null,
      sessions: [],
      messages: [],
      isLoading: false,
      error: null,

      createSession: (title = "New Chat") => {
        const sessionId = Date.now();
        const newSession: ChatSession = {
          id: sessionId,
          title,
          messages: [],
          createdAt: new Date(),
          updatedAt: new Date(),
        };
        set((state) => ({
          sessions: [newSession, ...state.sessions],
          currentSessionId: sessionId,
          messages: [],
        }));
        return sessionId;
      },

      setCurrentSession: (
  sessionId: number
) => {
  set({
    currentSessionId: sessionId,
  });
},
      setCurrentSessionId: (
  sessionId: number | null
) =>
  set({
    currentSessionId: sessionId,
  }),

      deleteSession: (sessionId: number) => {
        set((state) => {
          const newSessions = state.sessions.filter((s) => s.id !== sessionId);
          const newCurrentSessionId =
            state.currentSessionId === sessionId
              ? newSessions[0]?.id || null
              : state.currentSessionId;
          return {
            sessions: newSessions,
            currentSessionId: newCurrentSessionId,
            messages:
              newCurrentSessionId === sessionId
                ? []
                : newSessions.find((s) => s.id === newCurrentSessionId)?.messages || [],
          };
        });
      },

      updateSessionTitle: (sessionId: number, title: string) => {
        set((state) => ({
          sessions: state.sessions.map((s) =>
            s.id === sessionId ? { ...s, title, updatedAt: new Date() } : s
          ),
        }));
      },

      addMessage: (msg) => {
        const newMessage: ChatMessage = {
          ...msg,
          id: generateId(),
          timestamp: new Date(),
        };
        set((state) => {
          const updatedMessages = [...state.messages, newMessage];
          const updatedSessions = state.sessions.map((s) =>
            s.id === state.currentSessionId
              ? {
                  ...s,
                  messages: updatedMessages,
                  updatedAt: new Date(),
                  title:
                    s.messages.length === 0
                      ? msg.content.slice(0, 50) + (msg.content.length > 50 ? "..." : "")
                      : s.title,
                }
              : s
          );
          return {
            messages: updatedMessages,
            sessions: updatedSessions,
          };
        });
      },

      updateMessage: (messageId: string, updates: Partial<ChatMessage>) => {
        set((state) => {
          const updatedMessages = state.messages.map((m) =>
            m.id === messageId ? { ...m, ...updates } : m
          );
          const updatedSessions = state.sessions.map((s) =>
            s.id === state.currentSessionId
              ? { ...s, messages: updatedMessages, updatedAt: new Date() }
              : s
          );
          return {
            messages: updatedMessages,
            sessions: updatedSessions,
          };
        });
      },

      setLoading: (loading: boolean) => set({ isLoading: loading }),

      setError: (error: string | null) => set({ error }),

      clearMessages: () => set({ messages: [] }),
      setMessages: (
  messages: ChatMessage[]
) =>
  set({
    messages,
  }),
    })
  )
;
