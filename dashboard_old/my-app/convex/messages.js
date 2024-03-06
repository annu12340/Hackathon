import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const send = mutation({
    args: { message: v.string(), status: v.string() },
    handler: async (ctx, { message, status }) => {
      // Send a new message.
      await ctx.db.insert("messages", { message, status });
    },
});