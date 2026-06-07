export interface Citation {
  title: string;
  url: string;
  source?: string;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
  citations?: Citation[];
  isLoading?: boolean;
}

export interface ChatSession {
  id: number;
  title: string;
  messages: ChatMessage[];
  createdAt: Date;
  updatedAt: Date;
}
