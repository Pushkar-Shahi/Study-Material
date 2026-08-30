<div align="center">

# 🔴 Redis Deep Dive
### *In-Memory Data Structures, Messaging, Scripting & Performance*

![Progress](https://img.shields.io/badge/Sections-8-blue) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen) ![Platform](https://img.shields.io/badge/Platform-Redis-DC382D?logo=redis&logoColor=white)

</div>

---

## 📊 Table of Contents

| # | Section | Focus |
|---|-------|-------|
| 1️⃣ | 🟩 [Architecture, Setup & CLI](#-section-1--architecture-setup--cli) | Install, redis-cli, client-server model |
| 2️⃣ | 🟦 [Strings](#-section-2--strings) | SET/GET, numbers, TTL/expiration |
| 3️⃣ | 🟨 [Lists & Sets](#-section-3--lists--sets) | Ordered collections & unique unordered collections |
| 4️⃣ | 🟧 [Sorted Sets & HyperLogLog](#-section-4--sorted-sets--hyperloglog) | Scored ordering + probabilistic counting |
| 5️⃣ | 🟥 [Hashes](#-section-5--hashes) | Object-like field/value storage |
| 6️⃣ | 🟪 [Transactions & Pub/Sub](#-section-6--transactions--pubsub) | Atomic command groups + real-time messaging |
| 7️⃣ | 🟦‍⬛ [Lua Scripting & Geospatial](#-section-7--lua-scripting--geospatial) | Server-side logic + location data |
| 8️⃣ | ⬛ [Benchmarking & Server Management](#-section-8--benchmarking--server-management) | Performance testing, security, connections |

---

## 🧭 Quick-Reference Cheat Sheet

| Color | Section | Keywords |
|:---:|---|---|
| 🟩 | Architecture, Setup & CLI | `redis-server`, `redis-cli`, port 6379 |
| 🟦 | Strings | `SET`, `GET`, `MSET`, `INCR`, `EXPIRE`, `TTL` |
| 🟨 | Lists & Sets | `LPUSH`, `RPOP`, `SADD`, `SINTER`, `SUNION` |
| 🟧 | Sorted Sets & HyperLogLog | `ZADD`, `ZRANGE`, `PFADD`, `PFCOUNT` |
| 🟥 | Hashes | `HSET`, `HGETALL`, `HINCRBY` |
| 🟪 | Transactions & Pub/Sub | `MULTI`, `EXEC`, `WATCH`, `SUBSCRIBE`, `PUBLISH` |
| 🟦‍⬛ | Lua Scripting & Geospatial | `EVAL`, `EVALSHA`, `GEOADD`, `GEODIST` |
| ⬛ | Benchmarking & Server Mgmt | `redis-benchmark`, `AUTH`, `SELECT`, `CLIENT LIST` |

---

<br>

## <span style="color:#2E8B57">🟩 Section 1 — Architecture, Setup & CLI</span>

![Section](https://img.shields.io/badge/Section-1-2E8B57) ![Theme](https://img.shields.io/badge/Theme-Green_%E2%80%94_Getting_Running-2E8B57)

### ⚡ What Is Redis?

An **in-memory NoSQL database** known for extreme speed — capable of **110,000 writes** and **81,000 reads** per second.

| Trait | Detail |
|---|---|
| Architecture | Client-server model |
| Storage | Entire dataset lives in **primary memory** |
| Persistence | Can asynchronously save changes to disk |

### 🛠️ Setup

```bash
# Ubuntu package manager route
sudo apt update
sudo apt install redis-server

# Start the server
redis-server

# Open the CLI (default port 6379)
redis-cli
```

> 💡 Alternative install routes: Docker, or building from source — all available at `redis.io/download`.

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| In-memory storage | The source of Redis's extreme speed |
| `redis-server` | Starts the database process |
| `redis-cli` | Command-line interface, port 6379 by default |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#1E6FEB">🟦 Section 2 — Strings</span>

![Section](https://img.shields.io/badge/Section-2-1E6FEB) ![Theme](https://img.shields.io/badge/Theme-Blue_%E2%80%94_The_Simplest_Type-1E6FEB)

### 🔤 Core String Commands

| Command | Purpose |
|---|---|
| `SET key value` | Store a value |
| `GET key` | Retrieve a value |
| `MSET k1 v1 k2 v2` | Set multiple key-value pairs at once |
| `MGET k1 k2` | Retrieve multiple values at once |
| `GETRANGE key start end` | Get a substring (e.g., `0 4` for the first 5 chars) |
| `STRLEN key` | Total length of the string |
| `SETNX key value` | Set only if the key **doesn't already exist** |

### 🔢 Working with Numbers

Even though stored as strings, Redis handles numbers with **atomic precision**.

| Command | Effect |
|---|---|
| `INCR key` / `DECR key` | Add/subtract 1 |
| `INCRBY key n` / `DECRBY key n` | Add/subtract a specific amount |
| `INCRBYFLOAT key n` | Increment by a decimal value |

### ⏳ Data Expiration (TTL)

Perfect for caching sessions or temporary codes.

| Command | Purpose |
|---|---|
| `EXPIRE key seconds` | Set a timer on an existing key |
| `SETEX key seconds value` | Set a value **and** its expiry in one step |
| `TTL key` | Check how many seconds remain |

```bash
SET session:123 "active"
EXPIRE session:123 3600
TTL session:123          # → seconds remaining
```

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| SET/GET family | Basic key-value storage and retrieval |
| INCR/DECR family | Atomic numeric updates |
| EXPIRE/SETEX/TTL | Automatic data expiration |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#D4A017">🟨 Section 3 — Lists & Sets</span>

![Section](https://img.shields.io/badge/Section-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Collections-D4A017)

### 📋 Lists — Ordered Collections

| Command | Purpose |
|---|---|
| `LPUSH key value` / `RPUSH key value` | Add to the left / right of the list |
| `LRANGE key start stop` | Get a range (`0 -1` = everything) |
| `LINDEX key index` | Get item at a specific position |
| `LPOP key` / `RPOP key` | Remove & return first / last element |
| `LSET key index value` | Overwrite value at a position |
| `LINSERT key BEFORE\|AFTER pivot value` | Insert relative to an existing element |
| `LLEN key` | Total number of items |
| `LPUSHX` / `RPUSHX` | Only push if the list **already exists** |
| `SORT key [ALPHA]` | Sort the list (`ALPHA` for strings) |
| `BLPOP` / `BRPOP` | **Blocking** pop — waits until an item is available |

```bash
LPUSH mylist "a"
RPUSH mylist "b"
LRANGE mylist 0 -1   # → ["a", "b"]
```

### 🎯 Sets — Unique, Unordered Collections

Automatically **deduplicate** — adding an existing value is simply ignored.

| Command | Purpose |
|---|---|
| `SADD key member` | Add one or more elements |
| `SMEMBERS key` | List every unique element |
| `SISMEMBER key member` | 1 if present, 0 if not |
| `SCARD key` | Total element count (cardinality) |

### 🔀 Multi-Set Logic

| Command | Purpose |
|---|---|
| `SDIFF key1 key2` | Items in set 1 but **not** in set 2 |
| `SINTER key1 key2` | Items common to **both** sets |
| `SUNION key1 key2` | Merge into one unique collection |
| `SDIFFSTORE` / `SINTERSTORE` / `SUNIONSTORE` | Save comparison results into a new set |

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| Lists | Ordered, allow duplicates — great for queues/stacks |
| Blocking pops | Wait for data instead of returning empty |
| Sets | Unordered, unique — great for deduplication |
| SDIFF/SINTER/SUNION | Compare multiple sets against each other |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#E07B00">🟧 Section 4 — Sorted Sets & HyperLogLog</span>

![Section](https://img.shields.io/badge/Section-4-E07B00) ![Theme](https://img.shields.io/badge/Theme-Orange_%E2%80%94_Scoring_%26_Approximation-E07B00)

### 🏆 Sorted Sets (ZSets)

Like Sets, but each member has a **score** that keeps the set sorted min → max.

| Command | Purpose |
|---|---|
| `ZADD key score member` | Add a member with its score |
| `ZRANGE key start stop [WITHSCORES]` | Retrieve members by rank |
| `ZCARD key` | Total member count |
| `ZCOUNT key min max` | Count members within a score range |
| `ZREM key member` | Remove a specific member |
| `ZREMRANGEBYSCORE` / `ZREMRANGEBYRANK` | Remove a range of members |
| `ZSCORE key member` | Check a specific score |
| `ZINCRBY key increment member` | Adjust a score up/down |
| `ZREVRANGE` | Retrieve members highest → lowest score |

> 🌍 **Under the hood:** Redis stores **Geospatial** data using Sorted Sets — a 52-bit "geohash" becomes the score.

### 📊 HyperLogLog — Probabilistic Unique Counting

Counts unique values (IPs, search terms, emails) using a **tiny, fixed amount of memory** — an *approximate* count, ideal for huge datasets.

| Command | Purpose |
|---|---|
| `PFADD key element` | Add one or more items |
| `PFCOUNT key` | Approximate unique count |
| `PFCOUNT key1 key2` | Combined unique count across multiple keys |
| `PFMERGE dest src1 src2` | Permanently merge HLLs into a new key |

> 💡 Example use case: merge daily-unique-visitor HLLs into a weekly/monthly total.

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| ZSets | Sets with an ordering score — power rankings, leaderboards |
| Geospatial (under the hood) | Uses ZSet + geohash score |
| HyperLogLog | Fast, memory-cheap approximate unique counting |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#C0392B">🟥 Section 5 — Hashes</span>

![Section](https://img.shields.io/badge/Section-5-C0392B) ![Theme](https://img.shields.io/badge/Theme-Red_%E2%80%94_Object-Like_Storage-C0392B)

### 🗂️ Creating and Accessing Data

Maps of string fields → string values — perfect for objects like user profiles.

| Command | Purpose |
|---|---|
| `HSET key field value` | Add a single field |
| `HMSET key f1 v1 f2 v2` | Add multiple fields at once |
| `HGETALL key` | Return all fields and values |
| `HKEYS key` / `HVALS key` | Return only field names / only values |
| `HMGET key f1 f2` | Retrieve specific fields at once |

### 🔍 Management & Metadata

| Command | Purpose |
|---|---|
| `HEXISTS key field` | Check if a field is present |
| `HLEN key` | Total field count |
| `HSTRLEN key field` | Character length of a field's value |
| `HSETNX key field value` | Set only if the field **doesn't already exist** |

### 🧮 Atomic Updates and Deletion

| Command | Purpose |
|---|---|
| `HINCRBY key field n` | Increment an integer field |
| `HINCRBYFLOAT key field n` | Increment a decimal field |
| `HDEL key field` | Remove one or more fields |

```bash
HSET user:1 name "Aditya" age "25"
HGETALL user:1     # → name Aditya, age 25
HINCRBY user:1 age 1
```

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| HSET/HGETALL | Store and retrieve object-like data |
| HINCRBY/HINCRBYFLOAT | Atomic math on a specific field |
| HSETNX | Prevents accidental field overwrites |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#8E44AD">🟪 Section 6 — Transactions & Pub/Sub</span>

![Section](https://img.shields.io/badge/Section-6-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Purple_%E2%80%94_Atomicity_%26_Messaging-8E44AD)

### 🔒 Transactions

Execute a group of commands **atomically** — all or nothing.

| Command | Purpose |
|---|---|
| `MULTI` | Start transaction mode |
| *(any command)* | Gets **queued**, not executed immediately |
| `EXEC` | Fire all queued commands at once |
| `DISCARD` | Cancel the queued transaction |

```bash
MULTI
SET a 1
SET b 2
EXEC          # both commands run atomically
```

### 👀 Conditional Execution — WATCH

| Behavior | Detail |
|---|---|
| `WATCH key` | Monitor a key for changes |
| If the key changes before `EXEC` | The **entire transaction is blocked**, returns null |

> 💡 Useful for ensuring data hasn't been tampered with by another process mid-transaction.

### 📢 Pub/Sub — Real-Time Messaging

| Command | Purpose |
|---|---|
| `SUBSCRIBE channel` | Start listening for messages |
| `PUBLISH channel "message"` | Send data — returns subscriber count reached |

> 📡 Channels are created **dynamically** the moment a client subscribes — no setup needed.

### 🌟 Pattern-Based Subscriptions

| Pattern | Example | Matches |
|---|---|---|
| `*` (multi-char) | `news*` | `news1`, `news2`, `news_updates` |
| `?` (single-char) | `h?llo` | `hello`, `hallo` |
| `[]` (char set) | `b[ae]ll` | `ball`, `bill` |

### 🔎 Introspection

| Command | Purpose |
|---|---|
| `PUBSUB CHANNELS` | List all active (non-pattern) channels |
| `PUBSUB NUMSUB channel` | Count subscribers on a channel |
| `PUBSUB NUMPAT` | Total active pattern subscriptions |

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| MULTI/EXEC/DISCARD | Group commands into one atomic operation |
| WATCH | Conditional transaction execution based on key changes |
| SUBSCRIBE/PUBLISH | Core real-time messaging commands |
| PSUBSCRIBE | Wildcard-based channel subscriptions |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#008B8B">🟦‍⬛ Section 7 — Lua Scripting & Geospatial</span>

![Section](https://img.shields.io/badge/Section-7-008B8B) ![Theme](https://img.shields.io/badge/Theme-Teal_%E2%80%94_Server-Side_Power-008B8B)

### 📜 Lua Scripting

Run complex logic **directly on the server** for better performance.

| Feature | Detail |
|---|---|
| **Atomicity** | The entire script runs atomically — no other commands interleave |
| `EVAL` | Runs a script directly |
| `redis.call()` | Used inside scripts to interact with Redis data |
| `SCRIPT LOAD` + `EVALSHA` | Store script on server, run via hash to save bandwidth |
| **Timeout** | Default script timeout: **5 seconds** — keep scripts short |

```bash
EVAL "return redis.call('GET', KEYS[1])" 1 mykey
```

### 🌍 Geospatial Data

Store and query **longitude/latitude** coordinates.

| Detail | Description |
|---|---|
| Storage | Technically a **Sorted Set** — a 52-bit "geohash" is the score |
| Earth model | Spherical — introduces ~**0.5% margin of error** in distance calculations |
| Coordinate order | **Longitude first**, then latitude (`GEOADD`) |

| Command | Purpose |
|---|---|
| `GEOADD key lon lat member` | Add a location |
| `GEODIST key member1 member2` | Straight-line distance between two points |
| `GEORADIUS` / `GEORADIUSBYMEMBER` | Find locations within a radius |

```bash
GEOADD cities -122.4194 37.7749 "SanFrancisco"
GEODIST cities SanFrancisco NewYork km
```

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| EVAL / EVALSHA | Run (and efficiently re-run) Lua scripts server-side |
| Script atomicity | No other commands run mid-script |
| GEOADD | Store lon/lat as a geohash score in a Sorted Set |
| GEODIST / GEORADIUS | Distance and proximity queries |

[⬆ Back to top](#-table-of-contents)

---

<br>

## <span style="color:#2C3E50">⬛ Section 8 — Benchmarking & Server Management</span>

![Section](https://img.shields.io/badge/Section-8-2C3E50) ![Theme](https://img.shields.io/badge/Theme-Dark_%E2%80%94_Performance_%26_Security-2C3E50)

### 🏋️ Benchmarking

`redis-benchmark` measures how many requests/second your server can handle.

```bash
# Default test: all commands, 50 parallel clients, 3-byte payload
redis-benchmark

# Remote server
redis-benchmark -h 127.0.0.1 -p 6379
```

| Flag | Purpose |
|:---:|---|
| `-n` | Total number of requests (e.g., `-n 1000`) |
| `-d` | Payload size in bytes (e.g., `-d 100`) |
| `-c` | Number of parallel clients (e.g., `-c 200`) |

> 📉 **Real example:** ~31,000 `SET` req/sec with 3-byte strings, dropping to ~830 req/sec with 100KB strings.

### 🔌 Connection Health & Databases

| Command | Purpose |
|---|---|
| `PING` | Health check — returns `PONG` |
| `ECHO "message"` | Server repeats a string back |
| `SELECT <index>` | Switch between databases (default index 0) |

> ⚠️ Keys are **isolated per database index** — but in a **cluster configuration**, you're limited to database 0 only.

### 👥 Client Management

| Command | Purpose |
|---|---|
| `CLIENT LIST` | Show all active connections (ID, address, age) |
| `CLIENT SETNAME <name>` | Name your current connection |
| `CLIENT KILL <id>` | Disconnect a client |

### 🔐 Security & Remote Access

| Command | Purpose |
|---|---|
| `CONFIG SET requirepass <password>` | Set a password (none by default) |
| `AUTH <password>` | Required before any command once a password is set |
| `redis-cli -h <IP> -p <port>` | Connect to a remote server |

### 🧭 Summary Table

| Concept | Purpose |
|---|---|
| redis-benchmark | Load-tests the server under configurable conditions |
| PING/ECHO | Basic connection health checks |
| SELECT | Switch between isolated database indexes |
| CLIENT LIST/KILL | Monitor and manage active connections |
| requirepass / AUTH | Password-based access control |

[⬆ Back to top](#-table-of-contents)

---

<div align="center">

### 🎉 Redis Deep Dive Complete!
*From `redis-server` to atomic scripts, real-time messaging, and load-tested performance.*

</div>
