---
description: Secure Chat Notification
---

# Secure Chat

Template Editor

* Workbench
* Definitions
  * Contacts
  * PNN
  * Extension -> Push Notifications
* Criteria
  * PNN 200 - Recipient -> EMP 20670 -> Last Deparment Networking Most Recent
  * PNN 530 - Linked TLK Exists
  * PNN 100 - Chat Message
* Columns
  * **Send Instant (PNN) \[90504]**
  * **In App Text (PNN) \[90506]**
  * **Intended Recipients Summary (PNN) \[90525]**
  * **Linked Secure Chat Conversation (PNN) \[90520]**
  * **Notification Priority (PNN) \[90503]**
  * **Notification Title (PNN) \[90512]**
  * **Notification Type (PNN) \[90516]**
  * **Out of App Text (PNN) \[90511]**
  * **Push Notification ID (PNN) \[90502]**
  * **Recipient Count (PNN) \[90505]**
  * **Recipient Statuses (PNN) \[90521]**



**Secure Chat Conversation Template**

**Criteria**&#x20;

**-Last Login Department** TLK 2000 -> EMP -> 20670 -> Most Recent

-Includes participant

-Contact number = 1



Hyperlink: EpicAct:AC\_RW\_STATUS,RunParams:101171|3713451

* TLK 2000 -> EMP -> 20670 -> Most Recent&#x20;

#### Columns for Export. Custom Columns needed for Item return

```markup
| Pasted Label           | UI Field Name                                      |
|------------------------|-----------------------------------------------------|
| msg_id                | Chat Conversation ID [33165]                       |
| msg_contact_id        | CSN for TLK [105191]  |
| pt_id                 | HashedMRN [100636]                                |
| msg_users             | Chat Conversation Participants [33166]             |
| msg_users_count       | Chat Conversation Participant Count [33176]        |
| msg_log_count         | Chat Conversation Message Count [33175]            |
| msg_log_team          | tlk 2100 [100714]                                  |
| msg_log_txt           | tlk 3000 [100706]                                  |
| msg_log_send_time     | tlk 3100 [100708]                                  |
| msg_log_type          | tlk 3105 [100799]                                  |
| msg_log_send_user     | tlk 3110 [100711]                                  |
| access_user           | tlk 4000 [100712]                                  |
| access_time           | tlk 4010 [100713]                                  |
| access_msg_log_line   | tlk 4020 [100744]                                  |
| reaction_msg_log_line | tlk 3500 [100729]                                  |
| reaction_user         | tlk 3502 [100755]                                  |
| reaction_time         | tlk 3503 [100741] 
| msg_log_users         | tlk 2100
| msg_log_users_unread  | tlk 2060
| msg_log_users_affect  | tlk 3200
```

*
