# Privacy Policy for Social Fact Checker

Last Updated: August 30, 2025

## For End Users

### What Information We Collect

1. **Threads Content**
   - Public posts and replies that you interact with through our fact-checking service
   - Thread IDs and timestamps of posts being fact-checked
   - Public profile information visible on Threads

2. **Usage Data**
   - How you interact with our fact-checking service
   - Time and frequency of fact-check requests
   - Types of content you request fact-checking for

3. **Authentication Data**
   - Meta account tokens (required for Threads API access)
   - Basic profile information from Meta's authentication service

### How We Use Your Information

1. **Core Service Functionality**
   - To provide automated fact-checking of Threads posts
   - To post replies with fact-check results
   - To monitor specified threads for fact-checking requests

2. **Service Improvement**
   - To improve our fact-checking accuracy
   - To understand common misinformation patterns
   - To enhance user experience

3. **Legal Compliance**
   - To comply with Meta's platform policies
   - To maintain required records for legal purposes

### Data Protection

- All data is encrypted during transmission
- Access tokens are securely stored and never exposed
- We do not store your Threads password or direct login credentials
- Data is retained only as long as necessary for service operation

### Your Rights

You have the right to:
- Request access to your data
- Request deletion of your data
- Opt-out of the service
- Report issues or concerns

### Third-Party Services

We use:
- Meta's Threads API
- Fact-checking databases and services
- Content analysis tools

## For Developers

### Technical Implementation Details

1. **Data Storage**
   - Access tokens: Encrypted at rest
   - Thread IDs: Stored temporarily for monitoring
   - Fact-check results: Cached temporarily
   - No permanent storage of user content

2. **API Usage**
   - Meta Graph API v18.0
   - Threads API endpoints
   - OAuth 2.0 authentication flow

3. **Data Flow**
```
User Request → OAuth Authentication → Thread Monitoring → 
Fact Check Processing → Response Generation → Thread Reply
```

### Security Requirements

1. **Authentication**
   - Implement secure token storage
   - Use HTTPS for all API calls
   - Rotate access tokens periodically
   - Never log authentication credentials

2. **Data Handling**
   - Minimize data retention
   - Implement proper error handling
   - Log only necessary debugging information
   - Clean up temporary data regularly

3. **Compliance Requirements**
   - Follow Meta's Platform Terms
   - Implement rate limiting
   - Handle user data deletion requests
   - Maintain audit logs

### Development Guidelines

1. **API Integration**
   - Use official Meta SDKs when possible
   - Implement proper error handling
   - Follow Meta's best practices
   - Monitor API deprecation notices

2. **Testing**
   - Test with minimal permissions
   - Use test accounts for development
   - Implement monitoring for API limits
   - Regular security testing

3. **Deployment**
   - Use secure environment variables
   - Implement proper logging
   - Monitor API usage
   - Regular security updates

### Rate Limits and Quotas

1. **Meta API Limits**
   - Respect standard rate limits
   - Implement exponential backoff
   - Monitor usage quotas
   - Handle rate limit errors gracefully

2. **Service Limits**
   - Maximum concurrent requests
   - Cache expiration policies
   - Request timeouts
   - Error retry policies

## Contact Information

For privacy-related questions or concerns:
- Email: [Your Contact Email]
- Issues: [GitHub Issues URL]
- Security: [Security Contact]

## Updates to Privacy Policy

We may update this privacy policy as needed. Users will be notified of significant changes through:
- In-app notifications
- Email notifications (if provided)
- Updates to this document

## Compliance

This service complies with:
- Meta Platform Terms
- Meta Developer Policies
- Data Protection Regulations
- Content Moderation Guidelines

---

By using this service, you agree to this privacy policy and our terms of service.
