-- =========================================
-- Nistula Unified Messaging Platform Schema
-- =========================================


-- =========================================
-- Guests Table
-- One guest profile across all channels
-- =========================================

CREATE TABLE guests (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================
-- Reservations Table
-- Linked to guests and properties
-- =========================================

CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    guest_id INTEGER REFERENCES guests(id),
    booking_ref VARCHAR(100) UNIQUE NOT NULL,
    property_id VARCHAR(100) NOT NULL,
    check_in_date DATE,
    check_out_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================
-- Conversations Table
-- Groups multiple messages together
-- =========================================

CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    guest_id INTEGER REFERENCES guests(id),
    reservation_id INTEGER REFERENCES reservations(id),
    source VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================
-- Messages Table
-- Stores all inbound and outbound messages
-- =========================================

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    conversation_id INTEGER REFERENCES conversations(id),

    message_id UUID NOT NULL UNIQUE,

    sender_type VARCHAR(50) NOT NULL,
    source VARCHAR(50) NOT NULL,

    message_text TEXT NOT NULL,

    query_type VARCHAR(100),

    confidence_score DECIMAL(3,2),

    drafted_reply TEXT,

    action VARCHAR(50),

    is_ai_generated BOOLEAN DEFAULT FALSE,
    is_agent_edited BOOLEAN DEFAULT FALSE,
    is_auto_sent BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================
-- AI Metadata Table
-- Stores AI-specific processing details
-- =========================================

CREATE TABLE ai_message_metadata (
    id SERIAL PRIMARY KEY,

    message_id INTEGER REFERENCES messages(id),

    ai_model VARCHAR(100),
    prompt_tokens INTEGER,
    completion_tokens INTEGER,

    processing_status VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- =========================================
-- DESIGN DECISIONS
-- =========================================

-- 1. Separate conversations and messages tables:
--    A conversation can contain multiple inbound and outbound messages.
--    This keeps the schema scalable and avoids duplicating guest data.

-- 2. Unified messages table:
--    All channels (WhatsApp, Airbnb, Booking.com, Instagram)
--    are stored in one table using the source field.
--    This simplifies querying and analytics across platforms.

-- 3. AI workflow tracking:
--    The schema stores:
--      - confidence_score
--      - query_type
--      - drafted_reply
--      - auto-send status
--    This supports auditability and human review workflows.

-- 4. AI metadata separation:
--    AI processing details are stored separately from messages
--    to keep the main messaging table cleaner and extensible.

-- 5. Reservation linking:
--    Conversations are linked to reservations
--    so support history can be tied to actual guest bookings.